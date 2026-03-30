/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: '#27ae60',
        secondary: '#3498db',
        accent: '#e67e22',
      }
    },
  },
  plugins: [],
}
