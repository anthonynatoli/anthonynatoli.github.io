import React, { Component } from 'react';
import PropTypes from 'prop-types'

class BookCard extends Component {
    constructor(props) {
        super(props);
        
        this.state = {
            expanded: true
        };

        this.expandCard = this.expandCard.bind(this);
    }
    render() {
        const book = this.props.bookInfo.volumeInfo;
        const thumbnail = book.imageLinks.smallThumbnail;
        const name = book.title;
        const authors = book.authors.join(', ');

        let body = '';

        if (this.state.expanded) {
            body = (<div className="info-container">
                <div className="book-thumbnail">
                    <a href={book.previewLink} target="_blank"><img src={thumbnail} /></a>
                </div>
                <div className="book-summary" dangerouslySetInnerHTML={{__html: book.description}}>
                </div>
            </div>);
        }
        //TODO: fix html injection in .book-summary
        return (
            <div className="book-card">
                <div className="title-bar" onClick={this.expandCard}>
                    <div className="title">{book.title}</div>
                    <div className="authors">{authors}</div>
                </div>
                {body}
            </div>
        );
    }
    expandCard() {
        const currentlyExpanded = this.state.expanded;

        this.setState({
            expanded: !currentlyExpanded
        });
    }
}

BookCard.propTypes = {
    bookInfo: PropTypes.object
};

export default BookCard;
