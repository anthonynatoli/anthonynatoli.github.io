import React from 'react';
import ReactDOM from 'react-dom';
import { AppContainer } from 'react-hot-loader';

import App from './containers/app.jsx'

const render = (Component, id) => {
    ReactDOM.render(
        <AppContainer>
            {Component}
        </AppContainer>,
        document.getElementById(id)
    );
};

render(<App/>, 'app');

if (module.hot) {
    module.hot.accept('./containers/app.jsx', () => {
        render(<App />, 'app');
    });
}
