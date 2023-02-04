import classes from './styles/Navbar.module.css';
import { Link } from 'react-router-dom';
import logo from './assets/logo/demystify.png';

const Navbar = () => {
    const navOptions = [
        {name:'Home',link:'/'},
        {name:'Get started',link:'/get-started'}
    ];

    return(
        <div className={classes.navbar}>
            <div className={classes.logo}>
                <Link to='/'>
                    <img src={logo} alt="logo" className={classes.logoImg} />
                </Link>
            </div>
            <div className={classes.options}>
                <ul className={classes.menus}>
                    {
                        navOptions.map(
                            (opt) => {
                                return (
                                    <Link to={opt.link}>
                                        <li>{opt.name}</li>
                                    </Link>
                                );
                            }
                        )
                    }
                </ul>
            </div>
        </div>
    );
}

export default Navbar