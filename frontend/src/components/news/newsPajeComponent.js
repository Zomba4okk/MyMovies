import React from "react";
import NewsCommentComponent from "../newsComments/newsCommentsComponent.js"

const NewsPageComponent = ({ news }) => (
    <div className="root">
        <h3>{news.title}</h3>
        <div className="image-set">
            {news.image.image_file.map((image, i) =>
                    <img key={i} src={image} />   )}
        </div>
        <p>{news.context}</p>
        <div className="CommentsList">
            {news.comments.map((comment, i) =>
                <NewsCommentComponent  newsComment=comment user=User key={i}/>)}//!!!!!!!!use only container not component
        </div>
    </div>
);


NewsPageComponent.React.propTypes = {
    title: React.propTypes.string,
    context: React.propTypes.string,
//    image.image_file: React.propTypes.string
};

export default NewsCommentComponent;