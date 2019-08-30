import {combineReducers} from "redux";
import {routerReducer} from "react-router-redux";
import mainPageReducer from "./mainPageReducers";
import baseFrameReducer from "./baseFrameReducer";
import newsReducer from "./newsReducer";
import filmPageReducer from "./filmPageReducer";
import slideMenuReducer from "./slideMenuReducer";


const rootReducer = combineReducers({
    routing: routerReducer,
    mainPageReducer,
    baseFrameReducer,
    newsReducer,
    filmPageReducer,
    slideMenuReducer,
});

export default rootReducer;