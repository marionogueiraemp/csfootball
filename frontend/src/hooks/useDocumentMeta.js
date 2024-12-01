import { useEffect } from "react";

const useDocumentMeta = (title, description) => {
  useEffect(() => {
    document.title = `CS Football | ${title}`;
    const metaDescription = document.querySelector('meta[name="description"]');
    if (metaDescription) {
      metaDescription.setAttribute("content", description);
    }
  }, [title, description]);
};

export default useDocumentMeta;
