import React from 'react';
import PropTypes from 'prop-types';

class RunLogContainer extends React.Component {
    constructor (props) {
        super(props);

        this.state = {
            selectedMonth: 0,
            graphType: 'bar'
        };
    }
    render() {
        return (
            <div>this is my run log</div>
        );
    }
}

RunLogContainer.propTypes = {
    runData: PropTypes.object
};

export default RunLogContainer;
