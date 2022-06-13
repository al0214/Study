import React,{uesState, useState} from 'react';
import OddEvenResult from './OddEvenResult';

const Counter = ({initialValue}) => {
    // 0에서 출발
    // + 버튼을 누르면 1 추가
    // - 버튼을 누르면 1 빼기

    const [count, setCount] = useState(initialValue);

    const onIncrease = () => {
        setCount(count + 1);
    };

    const onDecrease = () => {
        setCount(count - 1);
    };

    return (
        <div>
            <h2>{count}</h2>
            <button onClick={onIncrease}>+</button>
            <button onClick={onDecrease}>-</button>
            <OddEvenResult count={count}/>
        </div>
    );
};

Counter.defaultProps = {
    initialValue: 0
}

export default Counter