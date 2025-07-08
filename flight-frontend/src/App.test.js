import { render, screen } from '@testing-library/react';
import App from './App';

test('renders welcome heading', () => {
  render(<App />);
  const heading = screen.getByText(/welcome to the flight booking system/i);
  expect(heading).toBeInTheDocument();
});