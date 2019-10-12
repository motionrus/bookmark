import * as React from "react"
import CardMedia from "@material-ui/core/CardMedia"
import CardContent from "@material-ui/core/CardContent"
import Typography from "@material-ui/core/Typography"
import CardActions from "@material-ui/core/CardActions"
import {deleteBookmark} from "reduxStore/action/bookmark"
import {connect} from "react-redux"
import {useStyles} from "components/CardContent/style"
import {Card} from "@material-ui/core"
import ExpandMoreIcon from "@material-ui/icons/ExpandMore"
import clsx from "clsx"
import IconButton from "@material-ui/core/IconButton"
import Collapse from "@material-ui/core/Collapse"
import BookmarkIcon from "@material-ui/icons/Bookmark"
import BookmarkBorderIcon from "@material-ui/icons/BookmarkBorder"
import DeleteForeverIcon from "@material-ui/icons/DeleteForever"
import ChevronRightIcon from "@material-ui/icons/ChevronRight"
import * as PropTypes from "prop-types"

export const BookmarkCardContent = ({
  deleteBookmark,
  description,
  image,
  pk,
  title,
  url,
}) => {
  const classes = useStyles()
  const [booked, setBooked] = React.useState(false)
  const [expanded, setExpanded] = React.useState(false)

  const handleBooked = () => {
    setBooked(!booked)
  }
  const handleExpandClick = () => {
    setExpanded(!expanded)
  }
  const handleDelete = (event) => {
    const {currentTarget: {dataset: {pk}}} = event
    deleteBookmark(pk)
  }

  return (
    <Card className={classes.card}>
      <CardMedia
        className={classes.cardMedia}
        image={image}
        title="Image title"
      />
      <CardContent className={classes.cardContent}>
        <Typography
          variant="subtitle1"
        >
          {title}
        </Typography>
      </CardContent>
      <CardActions disableSpacing>
        <IconButton href={url} color="primary" target="_blank">
          <ChevronRightIcon/>
        </IconButton>
        <IconButton
          color="primary"
          data-pk={pk}
          onClick={handleDelete}
        >
          <DeleteForeverIcon/>
        </IconButton>
        <IconButton
          aria-label="share"
          color="primary"
          onClick={handleBooked}
        >
          {booked ? <BookmarkIcon/> : <BookmarkBorderIcon/>}
        </IconButton>
        <IconButton
          aria-expanded={expanded}
          aria-label="show more"
          className={clsx(classes.expand, {
            [classes.expandOpen]: expanded,
          })}
          color="primary"
          onClick={handleExpandClick}
        >
          <ExpandMoreIcon/>
        </IconButton>
      </CardActions>
      <Collapse
        in={expanded}
        timeout="auto"
        unmountOnExit
      >
        <CardContent>
          <Typography>
            {description}
          </Typography>
        </CardContent>
      </Collapse>

    </Card>
  )
}

const mapDispatchToProps = {
  deleteBookmark,
}

export default connect(
  null,
  mapDispatchToProps,
)(BookmarkCardContent)

BookmarkCardContent.propTypes = {
  deleteBookmark: PropTypes.func,
  description: PropTypes.string,
  image: PropTypes.string,
  pk: PropTypes.number,
  title: PropTypes.string,
  url: PropTypes.string,
}
