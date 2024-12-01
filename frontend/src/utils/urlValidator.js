import { slugify } from "./slugify";

export const validateSlug = (currentSlug, name) => {
  const correctSlug = slugify(name);
  return currentSlug === correctSlug;
};
