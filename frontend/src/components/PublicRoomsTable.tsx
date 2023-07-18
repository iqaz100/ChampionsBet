import React from 'react';
import { Space, Table } from 'antd';
import type { ColumnsType } from 'antd/es/table';
import '../styles/PublicRoomsTable.css';

interface DataType {
  key: string;
  publicRooms: string;
  players: number;
  status: string;
}

const columns: ColumnsType<DataType> = [
  {
    title: 'Public rooms',
    dataIndex: 'publicRooms',
    key: 'publicRooms',
    width: 520,
    render: (text) => <a>{text}</a>,
  },
  {
    title: 'Players',
    dataIndex: 'players',
    key: 'players',
  },
  {
    title: 'Status',
    dataIndex: 'status',
    key: 'status',
  },
  {
    title: 'Action',
    key: 'action',
    render: (_, record) => (
      <Space size='middle'>
        <a>Join</a>
        <a>Show</a>
      </Space>
    ),
  },
];

const data: DataType[] = [
  {
    key: '1',
    publicRooms: 'fc kostomloty',
    players: 4,
    status: 'public',
  },
  {
    key: '2',
    publicRooms: 'Czarni wierzbno',
    players: 23,
    status: 'public',
  },
  {
    key: '3',
    publicRooms: 'Unia leszno',
    players: 7,
    status: 'public',
  },
];

export const PublicRoomsTable = () => (
  <Table columns={columns} dataSource={data} className='publicRoomTable' />
);
