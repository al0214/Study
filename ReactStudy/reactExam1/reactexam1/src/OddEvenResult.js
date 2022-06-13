const OddEvenResult = ({count}) => {
    return<>{count % 2 === 0 ? "짝수" : "홀수"}</>
};

export default OddEvenResult;

//부모 state가 변경되면서 Rerender되면 자식도 Rerender가 된다