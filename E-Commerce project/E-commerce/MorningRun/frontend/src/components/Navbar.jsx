function Navbar({
  user,
  cartCount,
  onProfile,
  onCart,
  onOrders,
  onAdmin,
  onLogout,
  onSignUp,
}) {
  return (
    <nav className="navbar">
      <div className="navbar-logo">
        <h2>MorningRun</h2>
      </div>

      <div className="navbar-account">
        {user ? (
          <>
            <span className="welcome-user">Hi, {user.first_name}</span>
            <button className="nav-button" onClick={onLogout}>
              Logout
            </button>
          </>
        ) : (
          <button className="nav-button" onClick={onSignUp}>
            Sign Up
          </button>
        )}
      </div>

      <div className="navbar-links">
        {!user && <a href="#home">Home</a>}
        <a href="#products">Products</a>
        {!user && <a href="#about">About Us</a>}
        {!user && <a href="#contact">Contact</a>}

        {user?.role === "customer" && (
          <button className="nav-button" onClick={onProfile}>
            Profile
          </button>
        )}

        {user?.role === "customer" && (
          <button className="nav-button" onClick={onCart}>
            Cart ({cartCount})
          </button>
        )}

        {user?.role === "customer" && (
          <button className="nav-button" onClick={onOrders}>
            Orders
          </button>
        )}

        {user?.role === "admin" && (
          <button className="nav-button" onClick={onAdmin}>
            Admin
          </button>
        )}

      </div>
    </nav>
  );
}

export default Navbar;
