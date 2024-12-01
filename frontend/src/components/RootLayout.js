import React from "react";
import { Provider } from "react-redux";
import store from "../store";
import { Outlet } from "react-router-dom";
import { MessageProvider } from "../context/MessageContext";
import ErrorBoundary from "./ErrorBoundary";
import NavigationProgress from "./NavigationProgress";
import Navbar from "./Navbar";
import Breadcrumb from "./Breadcrumb";
import PageTransition from "./PageTransition";

const RootLayout = () => {
  return (
    <Provider store={store}>
      <ErrorBoundary>
        <MessageProvider>
          <NavigationProgress />
          <Navbar />
          <div className="container mt-4">
            <Breadcrumb />
            <PageTransition>
              <Outlet />
            </PageTransition>
          </div>
        </MessageProvider>
      </ErrorBoundary>
    </Provider>
  );
};

export default RootLayout;
