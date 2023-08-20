import '../styles/LoginPage.css';
import React from 'react';
import { LoginForm } from './LoginForm';

export const LoginPage = () => {
  return (
    <>
      <div className='loginContainer'>
        <div className='leftSideLogin'>
          <h1 className='loginLogo'>
            <span className='logChampions'>Champions</span>
            <span className='logBet'>Bet</span>
          </h1>
          <div className='loginForm'>
            <LoginForm />
          </div>
        </div>
        <div className='rightSideLogin'></div>
      </div>
    </>
  );
};
