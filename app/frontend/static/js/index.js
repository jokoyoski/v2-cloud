import React from 'react';
import ReactDOM from 'react-dom';
import VmList  from '../react/components/VmList';

class IndexPage extends React.Component {
    constructor(props) {
        super(props);
        console.log("Index Page Constructor");
    }

    componentDidMount() {
        console.log("Index Page Init");
    }

    render() {
        return <VmList/>
    }
}
ReactDOM.render(<IndexPage />, document.getElementById('react-component'));
