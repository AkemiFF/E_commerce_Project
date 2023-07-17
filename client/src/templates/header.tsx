function Header() {
    return (
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">

            <div className="collapse navbar-collapse" id="navbarSupportedContent">
                <ul className="navbar-nav mr-auto">
                    <li className="nav-item active">
                        <a href="{% url 'index' %}">
                            <h1>AkemiShop</h1>
                        </a>
                    </li>
                    <li className="nav-item">

                        <a href="">Panier</a>

                    </li>
                    <li className="nav-item">

                        <a href="{% url 'logout' %}">Déconnexion</a>

                        <a href="{% url 'singup' %}">S'inscrire</a>
                        <a href="{% url 'login' %}">Connéxion</a>

                    </li>
                </ul>

            </div>
        </nav>
    );
}

export default Header;