function Header() {
    return (
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">

            <div className="collapse navbar-collapse" id="navbarSupportedContent">
                <ul className="navbar-nav mr-auto">
                    <li className="nav-item active">
                        <a href="">
                            <h1>Shop</h1>
                        </a>
                    </li>
                    <li className="nav-item">

                        <a href="">Panier</a>

                    </li>
                    <li className="nav-item">
                        <a href="">Déconnexion</a>
                        <a href="">S'inscrire</a>
                        <a href="">Connéxion</a>
                    </li>
                </ul>

            </div>
        </nav>
    );
}

export default Header;