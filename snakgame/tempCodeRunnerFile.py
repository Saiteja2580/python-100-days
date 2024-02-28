for tail in snake.segment_list:
        if snake.head.distance(tail) < 10:
            is_game_on = False
            score.game_over()