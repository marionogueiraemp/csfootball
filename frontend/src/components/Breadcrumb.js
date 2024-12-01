import React from "react";
import { Link, useLocation } from "react-router-dom";

const Breadcrumb = () => {
  const location = useLocation();
  const pathnames = location.pathname.split("/").filter((x) => x);

  return (
    <nav aria-label="breadcrumb">
      <ol className="breadcrumb">
        <li className="breadcrumb-item">
          <Link to="/">Home</Link>
        </li>
        {pathnames.map((name, index) => {
          const routeTo = `/${pathnames.slice(0, index + 1).join("/")}`;
          const isLast = index === pathnames.length - 1;

          return isLast ? (
            <li
              key={name}
              className="breadcrumb-item active"
              aria-current="page"
            >
              {name.charAt(0).toUpperCase() + name.slice(1)}
            </li>
          ) : (
            <li key={name} className="breadcrumb-item">
              <Link to={routeTo}>
                {name.charAt(0).toUpperCase() + name.slice(1)}
              </Link>
            </li>
          );
        })}
      </ol>
    </nav>
  );
};

export default Breadcrumb;
