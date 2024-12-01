import React, { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";

const NavigationProgress = () => {
  const [isNavigating, setIsNavigating] = useState(false);
  const location = useLocation();

  useEffect(() => {
    setIsNavigating(true);
    const timer = setTimeout(() => setIsNavigating(false), 500);
    return () => clearTimeout(timer);
  }, [location]);

  return (
    <div className={`navigation-progress ${isNavigating ? "active" : ""}`}>
      <div className="progress-bar"></div>
    </div>
  );
};

export default NavigationProgress;
