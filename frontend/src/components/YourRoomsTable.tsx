import React from 'react';
import { Space, Table } from 'antd';
import type { ColumnsType } from 'antd/es/table';
import '../styles/YourRoomsTable.css';

interface DataType {
  key: string;
  yourRooms: string;
  players: number;
  status: string;
}

const columns: ColumnsType<DataType> = [
  {
    title: 'Your rooms',
    dataIndex: 'yourRooms',
    key: 'yourRooms',
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
        <a>Quit</a>
        <a>Show</a>
      </Space>
    ),
  },
];

const data: DataType[] = [
  {
    key: '1',
    yourRooms: 'Bukmacherska Liga Mistrzów',
    players: 32,
    status: 'private',
  },
  {
    key: '2',
    yourRooms: 'FC Haszcze',
    players: 42,
    status: 'private',
  },
  {
    key: '3',
    yourRooms: 'Test',
    players: 32,
    status: 'private',
  },
];

export const YourRoomsTable = () => (
  <Table columns={columns} dataSource={data} className='roomTable' />
);
