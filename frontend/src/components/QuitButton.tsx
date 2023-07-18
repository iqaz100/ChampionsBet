import React, { useState } from 'react';
import { PoweroffOutlined } from '@ant-design/icons';
import { Button } from 'antd';
import '../styles/QuitButton.css';

export const QuitButton = () => {
  const [loadings, setLoadings] = useState<boolean[]>([]);

  const enterLoading = (index: number) => {
    setLoadings((prevLoadings) => {
      const newLoadings = [...prevLoadings];
      newLoadings[index] = true;
      return newLoadings;
    });

    setTimeout(() => {
      setLoadings((prevLoadings) => {
        const newLoadings = [...prevLoadings];
        newLoadings[index] = false;
        return newLoadings;
      });
    }, 6000);
  };

  return (
    <Button
      className='quitBtn'
      type='primary'
      icon={<PoweroffOutlined />}
      loading={loadings[1]}
      onClick={() => enterLoading(1)}
    >
      Log out
    </Button>
  );
};
