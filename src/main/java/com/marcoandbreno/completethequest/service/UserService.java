package com.marcoandbreno.completethequest.service;

import com.marcoandbreno.completethequest.model.User;
import com.marcoandbreno.completethequest.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

@Service
public class UserService {
  @Autowired
  private UserRepository userRepository;

  @Autowired
  private PasswordEncoder passwordEncoder;

  public User registerNewUserAccount(User user) {
    String encryptedPassword = passwordEncoder.encode(user.getPassword());
    user.setPassword(encryptedPassword);
    return userRepository.save(user);
  }

  public Long getUserIdByUsername(String username) {
    User user = userRepository.findByUsername(username);
    if (user != null) {
      return user.getId();
    }
    return null;
  }

  public boolean isUsernameUnique(String username) {
    // Check if the username already exists in the database
    User existingUser = userRepository.findByUsername(username);
    return existingUser == null;
  }
}
