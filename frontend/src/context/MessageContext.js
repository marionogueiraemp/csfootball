import React, { createContext, useState, useContext } from "react";

const MessageContext = createContext();

export const MessageProvider = ({ children }) => {
  const [message, setMessage] = useState(null);

  const showMessage = (text, type = "success", duration = 3000) => {
    setMessage({ text, type });
    setTimeout(() => setMessage(null), duration);
  };

  return (
    <MessageContext.Provider value={{ message, showMessage }}>
      {children}
      {message && (
        <div className={`alert alert-${message.type} message-toast`}>
          {message.text}
        </div>
      )}
    </MessageContext.Provider>
  );
};

export const useMessage = () => useContext(MessageContext);
