import React from 'react';
import PropTypes from 'prop-types';
import BookCard from '../components/bookCard.jsx';

import '../styles/bookLog.scss';

class BookLogContainer extends React.Component {
    constructor (props) {
        super(props);
        //
        // this.state = {
        //     bookList: []
        // };
    }
    // componentWillMount() {
    //     // make request to server, set prop
    //     console.log('will mount with:', this.state);
    //     const req = new Request('http://localhost:5000/books');
    //     fetch(req).then(resp => resp.json()).then(resp => {
    //         this.setState({
    //             bookList: resp
    //         });
    //         console.log(this.state);
    //     }, this);
    // }
    render() {
        const cards = this.props.bookList.map(book => (<BookCard bookInfo={book} />));
        return (<div>
            <div>BOOKS</div>
            <div className="cards-container">
                {cards}
            </div>
        </div>);
    }
}

BookLogContainer.propTypes = {
    bookList: PropTypes.array
};

export default BookLogContainer;
