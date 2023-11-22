import { Link } from 'react-router-dom';

const NavBar = () => {
    return (
        <nav className="main-nav">
            <ul>
                <li><Link to="/">HOME</Link></li>
                <li><Link to="/about">ABOUT</Link></li>
                <li><Link to="/characters">CHARACTERS</Link></li>\
                <li><Link to="/favorites">FAVORITES</Link></li>
            </ul>
        </nav>
    );
}

export default NavBar;