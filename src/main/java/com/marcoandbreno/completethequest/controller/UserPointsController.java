package com.marcoandbreno.completethequest.controller;

import com.marcoandbreno.completethequest.service.UserPointsService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/points")
public class UserPointsController {
  private final UserPointsService userPointsService;

  public UserPointsController(UserPointsService userPointsService) {
    this.userPointsService = userPointsService;
  }

 

  @GetMapping("/user-points")
  public String showUserPoints(Model model) {
    model.addAttribute("userPoints", userPointsService.getAllUserPoints());
    return "leaderboard"; // Assuming leaderboard.html is your template
  }
}
