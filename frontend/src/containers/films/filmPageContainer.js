import React from "react";
import { connect } from "react-redux";
import filmPageComponent from "../../components/films/filmPageComponent";
import {rateFilm, openModal} from "../../actions/filmsActions";

const mapStateToProps = state => ({
    film: state.filmPageReducer.film,
});

const mapDispatchToProps = (dispatch, ownProps) => ({
    openModal(item) {
        dispatch(openModal(item))
    },
    rateFilm(id, rating) {
        dispatch(rateFilm(id, rating))
    }
});

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(filmPageComponent)


