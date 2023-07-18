import '../styles/HomePage.css';
import React from 'react';
import { HomeMenu } from './HomeMenu';
import { QuitButton } from './QuitButton';
import { Profile } from './Profile';
import { YourRoomsTable } from './YourRoomsTable';
import { Button } from 'antd';
import { PublicRoomsTable } from './PublicRoomsTable';

export const HomePage = () => {
  return (
    <>
      <div className='container'>
        <div className='leftSide'>
          <h1 className='logo'>
            <span className='champions'>Champions</span>
            <span className='bet'>Bet</span>
          </h1>
          <Profile />
          <HomeMenu />
          <QuitButton />
        </div>
        <div className='rightSide'>
          <div className='roomsContainer'>
            <h1 className='roomsHeader'>Rooms:</h1>
            <div className='roomButtons'>
              <Button className='createRoomBtn'>Create room</Button>
              <Button className='joinRoomBtn'>Join room</Button>
            </div>
          </div>
          <YourRoomsTable />
          <PublicRoomsTable />
        </div>
      </div>
    </>
  );
};
