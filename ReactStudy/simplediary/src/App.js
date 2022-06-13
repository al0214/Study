import React, { useRef, useState } from "react";
import "./App.css";
import DiaryEditer from "./DiaryEditer";
import DiaryList from "./DiaryList.js";

// const dummyList = [
// {
//   id: 1,
//   author: "김재우",
//   content: "하이",
//   emotion: 1,
//   create_date: new Date().getTime(),
// },
// {
//   id: 2,
//   author: "최예성",
//   content: "하이 1",
//   emotion: 1,
//   create_date: new Date().getTime(),
// },
// {
//   id: 3,
//   author: "최진양",
//   content: "하이 2",
//   emotion: 1,
//   create_date: new Date().getTime(),
// },
// {
//   id: 4,
//   author: "정재성",
//   content: "하이 3",
//   emotion: 1,
//   create_date: new Date().getTime(),
// },
// ];

const App = () => {
  const [data, setData] = useState([]);

  const dataID = useRef(0);

  const onCreate = (author, content, emotion) => {
    const create_date = new Date().getTime();
    const newItem = {
      author,
      content,
      emotion,
      create_date,
      id: dataID.current,
    };
    dataID.current += 1;
    setData([newItem, ...data]);
  };

  const onDelete = (targetId) => {
    console.log(`${targetId}가 삭제되었습니다.`);
    const newDiaryList = data.filter((it) => it.id !== targetId);
    setData(newDiaryList);
  };

  const onEdite = (targetId, newContent) => {
    setData(data.map((it) => (it.id === targetId ? { ...it, content: newContent } : it)));
  };

  return (
    <div className="App">
      <DiaryEditer onCreate={onCreate} />
      <DiaryList onEdit={onEdite} diaryList={data} />
    </div>
  );
};

export default App;
