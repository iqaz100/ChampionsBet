import React from 'react';
import './styles/App.css';
import { LoginPage } from './components/LoginPage';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { HomePage } from './components/HomePage';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route
          path='/'
          element={
            <div className='App'>
              <LoginPage />
            </div>
          }
        ></Route>
        <Route
          path='/Home'
          element={
            <div className='App'>
              <HomePage />
            </div>
          }
        ></Route>
      </Routes>
    </Router>
  );
};

export default App;
