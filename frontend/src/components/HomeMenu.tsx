import React, { ReactNode, Key } from 'react';
import '../styles/HomeMenu.css';
import {
  AppstoreOutlined,
  CalendarOutlined,
  LinkOutlined,
  MailOutlined,
  SettingOutlined,
} from '@ant-design/icons';
import { Menu } from 'antd';
import type { MenuProps } from 'antd/es/menu';

type MenuItem = Required<MenuProps>['items'][number];

function getItem(
  label: ReactNode,
  key?: Key | null,
  icon?: ReactNode,
  children?: MenuItem[],
): MenuItem {
  return {
    key,
    icon,
    children,
    label,
  } as MenuItem;
}

const items: MenuItem[] = [
  getItem("What's new?", '1', <MailOutlined />),
  getItem('Rooms', '3', <AppstoreOutlined />),
  getItem('Settings', '4', <SettingOutlined />),
  getItem('FAQ', '2', <CalendarOutlined />),
];

export const HomeMenu = () => {
  return (
    <>
      <Menu
        style={{ width: 256 }}
        defaultSelectedKeys={['1']}
        defaultOpenKeys={['sub1']}
        mode='inline'
        items={items}
        className='home-menu'
      />
    </>
  );
};
