import { NavLink } from 'react-router-dom';

function Nav() {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-success">
      <div className="container-fluid">
        <NavLink className="navbar-brand" to="/">CarCar</NavLink>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
              <li className="nav-item">
                  <NavLink className="nav-link" aria-current="page" to="/manufacturers">Manufacturer List</NavLink>
              </li>
              <li className="nav-item">
                  <NavLink className="nav-link" aria-current="page" to="/manufacturers/new">New Manufacturer</NavLink>
              </li>
              <li className="nav-item">
                  <NavLink className="nav-link" aria-current="page" to="/models">Model List</NavLink>
              </li>
              <li className="nav-item">
                  <NavLink className="nav-link" aria-current="page" to="/models/new">New Model</NavLink>
              </li>
              <li className="nav-item">
                  <NavLink className="nav-link" aria-current="page" to="/technician">Enter a Technician</NavLink>
              </li>
              <li className="nav-item dropdown">

                  <NavLink className="nav-link" aria-current="page" to="/services">Appointment List</NavLink>
              </li>
              <li className="nav-item">
                  <NavLink className="nav-link" aria-current="page" to="/services/new/">New Service Appointment</NavLink>
              </li>
              <li className="nav-item">
                  <NavLink className="nav-link" aria-current="page" to="/services/history/">History of Appointments</NavLink>
              </li>
              <li className="nav-item">
                  <NavLink className="nav-link" aria-current="page" to="/salesperson/new/">New Sales Person</NavLink>
              </li>
              <li className="nav-item">
                  <NavLink className="nav-link" aria-current="page" to="/automobiles">Automobile List</NavLink>
              </li>
              <li className="nav-item">
                  <NavLink className="nav-link" aria-current="page" to="/automobiles/new/">New Automobile</NavLink>
              </li>
              <li className="nav-item">
                  <NavLink className="nav-link" aria-current="page" to="/customers/new/">New Potential Customer</NavLink>
              </li>
              <li className="nav-item">
                  <NavLink className="nav-link" aria-current="page" to="/salesrecords/">List Sales Record</NavLink>
              </li>
              <li className="nav-item">
                  <NavLink className="nav-link" aria-current="page" to="/salesrecords/new/">New Sales Record</NavLink>
              </li>
              <li className="nav-item">
                  <NavLink className="nav-link" aria-current="page" to="/saleshistory">Sales History</NavLink>
              </li>
          </ul>
        </div>
      </div>
    </nav>
  )
}

export default Nav;

