import classes from './styles/Homepage.module.css';
import { Link } from 'react-router-dom';

const HomePage = () => {
    return(
        <div className={classes.container}>
            <div className={classes['inner-container']}>
                <h3 className={classes.quote}>Think before you believe , predict Fakes easily!!</h3>
                <Link to='/get-started'>
                    <button className={classes.primary}>
                        Get Started
                    </button>
                </Link>
            </div>
        </div>
    );
}

export default HomePage;