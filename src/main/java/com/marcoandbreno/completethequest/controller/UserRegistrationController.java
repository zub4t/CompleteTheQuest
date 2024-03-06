package com.marcoandbreno.completethequest.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import com.marcoandbreno.completethequest.model.User;
import com.marcoandbreno.completethequest.service.UserService;

@Controller
@RequestMapping("/register")
public class UserRegistrationController {

    @Autowired
    private UserService userService;

    @GetMapping
    public ModelAndView showRegistrationForm() {
        ModelAndView mav = new ModelAndView("register");
        mav.addObject("user", new User());
        return mav;
    }

    @PostMapping
    public String registerUserAccount(User user, Model model) {
        if (userService.isUsernameUnique(user.getUsername())) {
            userService.registerNewUserAccount(user);
            return "redirect:/login";
        } else {
            // Add an error message to the model to indicate that the username is not unique
            model.addAttribute("errorMessage", "Username is already taken. Please choose another username.");
            return "register"; // Return to the registration page with the error message
        }
    }
}
