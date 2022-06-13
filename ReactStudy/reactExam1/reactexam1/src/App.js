import React from 'react';
//import './App.css';
//import MyFooter from './MyFooter';
import MyHeader from './MyHeader';
import Counter from './Counter';
import Container from './Container';

function App() {
 
  
  const style = {
    App: {
      backgroundColor: "black",
    },
    h2: {
      color: "red",
    },
    bold_text: {
      color: "green",
    },
  };

  const func = () => {
    return 'funk';
  }

  const number = 5;

  // return (
  //   <div style={style.App}>
  //     <MyHeader />
  //       <header className="App-header">
  //         <h2 style={style.h2}>
  //           안녕 리액트
  //         </h2>
  //         <b id='bold_text' style={style.bold_text}>
  //           {number}는 : {number % 2 === 0 ? '짝수' : '홀수'}
  //         </b>
  //       </header>
  //   </div>
  // );

  const counterProps = {
    a: 1,
    b: 2,
    c: 3,
    d: 4,
    e: 5,
    initialValue: 5,
  }


  return (
    <Container>
      <div>
        <MyHeader />
        <Counter {...counterProps}/>
      </div>
    </Container>
  )
}

export default App;
