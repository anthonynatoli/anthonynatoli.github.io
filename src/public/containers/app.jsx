import React from 'react';

import HomeContainer from './home.jsx';
import RunLogContainer from './run_log.jsx';

import '../styles/app.scss';

const contentMap = {
    'home': <HomeContainer />,
    'run_log': <RunLogContainer />
};

class App extends React.Component {
    constructor (props) {
        super(props);

        this.state = {
            selectedContent: 'home'
        };

        this.setContent = this.setContent.bind(this);
    }
    setContent (event) {
        const selectedContent = event.target.getAttribute('data');
        this.setState({
            selectedContent
        });
    }
    render () {
        const { selectedContent } = this.state;
        const content = contentMap[selectedContent];
        return (<div>
            <div className="header">
                <div className="background-image">
                    <img src="./src/public/images/cliff.jpg"></img>
                </div>
                <div className="links">
                    <button onClick={this.setContent} data="home">Home</button>
                    <button onClick={this.setContent} data="run_log">Run log</button>
                </div>
            </div>
            <div className="content">
                {content}
            </div>
        </div>);
    }
};

export default App;
