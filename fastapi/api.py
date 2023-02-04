from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware 
import uvicorn
from PIL import Image 
import torch.nn.functional as F 
import torch
from torchvision import transforms as T  
from torchvision.models import resnet50
from torch import nn 
import requests 

app = FastAPI() 

origins = [
    "http://localhost",
    "http://localhost:3000",
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# setting CPU to make predictions
device = torch.device("cpu")

# load pretrained model
model = resnet50(pretrained=True) #load pretrained model 
model.fc = nn.Linear(in_features=2048,out_features = 2, bias=True) 
model.load_state_dict(torch.load('car_alex_25.pt')) # load the model
model.to(device) 

# labels
class_map = ['defect','non-defect']

# prediction function
def predict_img(image): 

    INPUT_DIM = 224 
    preprocess = T.Compose([
            T.Resize(INPUT_DIM ),
            T.CenterCrop(224),
            T.ToTensor(),
            T.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )]) 
    

    im = Image.open(image).convert('RGB')
    im_preprocessed = preprocess(im) 
    batch_img_tensor = torch.unsqueeze(im_preprocessed, 0)
    output = model(batch_img_tensor) 
    confidence = F.softmax(output, dim=1)[0] * 100  

    # convert to list 
    confidence = confidence.tolist() 
    return confidence

# prediction function
def predict_img_url(url): 

    INPUT_DIM = 224 
    preprocess = T.Compose([
            T.Resize(INPUT_DIM ),
            T.CenterCrop(224),
            T.ToTensor(),
            T.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )]) 
    

    im = Image.open(requests.get(url, stream=True).raw).convert('RGB')
    im_preprocessed = preprocess(im) 
    batch_img_tensor = torch.unsqueeze(im_preprocessed, 0)
    output = model(batch_img_tensor) 
    confidence = F.softmax(output, dim=1)[0] * 100 

    # convert to list 
    confidence = confidence.tolist() 
    return confidence


@app.get("/")
async def root():
    return {"message": "Fake ID prediction"} 

@app.post("/url/")
async def create_url( url : str):       
    # send file to prediction function 
    prediction = predict_img_url(url)
    print(prediction)
    return {
        "defect": prediction[0], 
        "non-defect": prediction[1]
    }

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):       
    print(file)
    # send file to prediction function 
    prediction = predict_img(file.file) 
    print(prediction)
    return {
        "defect": prediction[0], 
        "non-defect": prediction[1]
    }

 
if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)