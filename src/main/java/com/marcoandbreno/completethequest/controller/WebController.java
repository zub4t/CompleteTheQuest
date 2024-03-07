package com.marcoandbreno.completethequest.controller;

import com.marcoandbreno.completethequest.common.DailyQuest;
import com.marcoandbreno.completethequest.model.User;
import com.marcoandbreno.completethequest.repository.FreqRepository;
import com.marcoandbreno.completethequest.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.Authentication;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class WebController {
  @Autowired
  private FreqRepository freqRepository;

  @Autowired
  private UserRepository userRepository;



  @GetMapping("/login")
  public String showLoginPage(Authentication authentication) {
    // Redirects to the homepage if the user is already logged in
    if (authentication != null && authentication.isAuthenticated()) {
      return "redirect:/index";
    }

    return "login"; // Returns the login view if the user is not authenticated
  }

  @GetMapping("/")
  public String showIndexPage(Model model, Authentication authentication) {

    User user = userRepository.findByUsername(authentication.getName());
    boolean exists = freqRepository.findByUserId(user.getId()).size() > 0;

    if (exists) {
      return "redirect:/points/user-points";
    } else {
      model.addAttribute("username", user.getUsername());

      model.addAttribute("question", DailyQuest.question);
      return "index";
    }

   


  }
}
