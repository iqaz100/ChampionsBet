import '../styles/ChampionsBet.css';
import { LoginForm } from './LoginForm';
import { UserProfile } from './UserProfile';

export const ChampionsBet = () => {
  return (
    <>
      <div className='container'>
        <div className='leftSide'>
          <h1 className='logo'>
            <span className='champions'>Champions</span>
            <span className='bet'>Bet</span>
          </h1>
          <div className='form'>
            <UserProfile />
            <LoginForm />
          </div>
        </div>
        <div className='rightSide'></div>
      </div>
    </>
  );
};
