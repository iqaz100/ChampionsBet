import React from 'react';
import { UserOutlined } from '@ant-design/icons';
import { Avatar, Space } from 'antd';
import '../styles/Profile.css';

export const Profile = () => (
  <Space direction='vertical' size={16} className='avatarSpace'>
    <Space wrap size={16}>
      <Avatar size={100} icon={<UserOutlined />} />
    </Space>
  </Space>
);
