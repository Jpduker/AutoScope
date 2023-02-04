import { Route, Routes } from "react-router-dom";
import HomePage from "../components/HomePage";
import CheckerPage from "../components/CheckerPage";

const Routs = () => {
    return (
        <Routes>
            <Route path="/get-started" element={<HomePage />} />
            <Route exact path="/" element={ <CheckerPage/> } />
        </Routes >
    );
}
export default Routs;