export const handleApiError = (error) => {
  if (error.response) {
    const status = error.response.status;
    const data = error.response.data;

    switch (status) {
      case 400:
        return `Invalid request: ${data.message || "Bad Request"}`;
      case 401:
        return "Authentication required. Please login.";
      case 403:
        return "You do not have permission to perform this action.";
      case 404:
        return "The requested resource was not found.";
      case 500:
        return "Server error. Please try again later.";
      default:
        return "An unexpected error occurred.";
    }
  }
  return "Network error. Please check your connection.";
};
