import React from 'react';

import HomeContainer from './home.jsx';
import RunLogContainer from './run_log.jsx';
import BookLogContainer from './book_log.jsx';

import '../styles/app.scss';

const contentMap = {
    'home': <HomeContainer />,
    'run_log': <RunLogContainer />,
    'book_log': <BookLogContainer />
};

class App extends React.Component {
    constructor (props) {
        super(props);

        this.state = {
            selectedContent: {
                page: 'home',
                props: ''
            },
            bookList: []
        };

        this.setContent = this.setContent.bind(this);
    }
    setContent (event) {
        const selectedContent = {
            page: event.target.getAttribute('data'),
            props: event.target.getAttribute('data-passProps')
        };
        this.setState({
            selectedContent
        });
    }
    componentWillMount() {
        // make request to server, set prop
        console.log('will mount with:', this.state);
        const req = new Request('http://localhost:5000/books');
        fetch(req).then(resp => resp.json()).then(resp => {
            this.setState({
                bookList: resp
            });
            console.log(this.state);
        }, this);
    }
    render () {
        const { selectedContent } = this.state;
        const passingProps = {};
        passingProps[selectedContent.props] = this.state[selectedContent.props];
        const content = React.cloneElement(contentMap[selectedContent.page], passingProps);
        return (<div>
            <div className="header">
                <div className="background-image">
                    <img src="./src/public/images/cliff.jpg"></img>
                </div>
                <div className="links">
                    <button onClick={this.setContent} data="home">Home</button>
                    <button onClick={this.setContent} data="run_log">Run log</button>
                    <button onClick={this.setContent} data="book_log" data-passProps="bookList">Book log</button>
                </div>
            </div>
            <div className="content">
                {content}
            </div>
        </div>);
    }
};

export default App;
