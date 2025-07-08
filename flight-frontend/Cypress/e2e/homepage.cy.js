describe('Homepage', () => {
  it('loads successfully', () => {
    cy.visit('http://localhost:3000')
    cy.contains('Welcome to the Flight Booking System') // Update if needed
  })
})