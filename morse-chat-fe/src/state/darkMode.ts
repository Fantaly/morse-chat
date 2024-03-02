/* ==========================================================================
  Holds dark mode state across the whole app,
  to be accessed from different componenents
========================================================================== */

import { ref, watchEffect, type Ref } from "vue";

type ColorScheme = "dark" | "light";

/**
 * Gets currently saved theme or browser preferred scheme
 */
const getTheme = (): ColorScheme => {
  const preferredDark = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
  const userTheme = localStorage.getItem("zulla-theme") as ColorScheme;
  return userTheme || (preferredDark ? "dark" : "light");
};

/**
 * Saves theme to storage and sets class to document
 * @param theme
 */
const setTheme = (theme: ColorScheme) => {
  activeTheme.value = theme;
  localStorage.setItem("morseCodeChat-theme", theme);

  if (theme === "dark") {
    document.body.classList.add("is-dark");
  } else {
    document.body.classList.remove("is-dark");
  }
};

const activeTheme: Ref<ColorScheme> = ref(getTheme());
export const isDark: Ref<boolean> = ref(activeTheme.value === "dark" ? true : false);

/**
 *  Watches changes on isDark ref and sets theme accordingly
 */
watchEffect(() => {
  if (isDark.value) {
    setTheme("dark");
  } else {
    setTheme("light");
  }
});
