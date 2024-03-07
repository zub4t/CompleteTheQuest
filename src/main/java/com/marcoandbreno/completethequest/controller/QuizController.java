package com.marcoandbreno.completethequest.controller;

import com.marcoandbreno.completethequest.common.DailyQuest;
import com.marcoandbreno.completethequest.model.User;
import com.marcoandbreno.completethequest.model.UserPoints;
import com.marcoandbreno.completethequest.repository.UserPointsRepository;
import com.marcoandbreno.completethequest.repository.UserRepository;
import com.marcoandbreno.completethequest.service.UserService;
import java.util.Optional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.Authentication;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class QuizController {
  @Autowired
  private UserRepository userRepository;

  @Autowired
  private UserPointsRepository userPointsRepository;

  @Autowired
  private UserService userService;

  @PostMapping("/submit")
  public String submitAnswer(
    @RequestParam("answer") String answer,
    Model model,
    Authentication authentication
  ) {
    String username = authentication.getName();
    Long userId = userService.getUserIdByUsername(username);

    boolean isCorrect = answer.equalsIgnoreCase(
      DailyQuest.answer.toLowerCase()
    );

    User user = userRepository.findById(userId).orElse(null);
    if (user == null) {
      model.addAttribute("message", "User not found.");
      return "index";
    }

    // Use Optional to handle both present and absent cases for UserPoints
    Optional<UserPoints> optionalUserPoints = userPointsRepository.findByUserId(
      userId
    );

    UserPoints userPoints = optionalUserPoints.orElseGet(() -> null);
    if (userPoints == null) {
      userPoints = new UserPoints();
      userPoints.setId(userId);
      userPoints.setUser(user);
      userPoints.setPoints(0);
    }

    if (isCorrect) {
      userPoints.setPoints(userPoints.getPoints() + 1);
      model.addAttribute("message", "Congratulations! Your answer is correct.");
      userPointsRepository.save(userPoints);
      return "redirect:/points/user-points";
    } else {
      model.addAttribute("message", "Sorry, your answer is incorrect.");
    }
    model.addAttribute("question", DailyQuest.question);
    model.addAttribute("username", username);

    return "index";
  }
}
