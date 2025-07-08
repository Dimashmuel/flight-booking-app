describe('Homepage', () => {
  it('loads successfully', () => {
    cy.visit('http://localhost:3000')
    cy.contains('Flight Booking App') // Update if needed
  })
})