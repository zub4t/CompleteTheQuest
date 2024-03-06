package com.marcoandbreno.completethequest.controller;

import com.marcoandbreno.completethequest.common.DailyQuest;
import org.springframework.security.core.Authentication;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class WebController {

  @GetMapping("/login")
  public String showLoginPage(Authentication authentication) {
    // Redirects to the homepage if the user is already logged in
    if (authentication != null && authentication.isAuthenticated()) {
      return "redirect:/index";
    }

    return "login"; // Returns the login view if the user is not authenticated
  }

  @GetMapping("/index")
  public String showIndexPage(Model model, Authentication authentication) {
    String username = authentication.getName();
    model.addAttribute("username", username);

    // Read the content of the file and set it as the question attribute
    model.addAttribute("question", DailyQuest.question);

    return "index";
  }

 
}
