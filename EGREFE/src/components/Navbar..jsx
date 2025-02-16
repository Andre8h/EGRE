import React from "react";

const Navbar = () => {
    return (
        <nav className="navbar">
            <div className="navbar-left">
                <ul className="links">
                    <li> 
                        <a href="#" className="user-library">Library</a> 
                    </li>
                    <li> 
                        <a href="#" className="user-imports">Import</a> 
                    </li>
                </ul>
            </div>
            <div className="navbar-right">
                <a href="#" className="user-icon">
                    <i></i>
                </a>
            </div>
        </nav>
    );
};

export default Navbar;