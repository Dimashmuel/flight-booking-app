const { defineConfig } = require('cypress')

module.exports = defineConfig({
  e2e: {
    baseUrl: 'http://localhost:3000',
    specPattern: 'Cypress/e2e/**/*.cy.{js,jsx,ts,tsx}',
    supportFile: false,
  },
})