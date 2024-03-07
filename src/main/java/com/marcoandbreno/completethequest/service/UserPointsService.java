package com.marcoandbreno.completethequest.service;

import java.util.List;

import org.springframework.stereotype.Service;

import com.marcoandbreno.completethequest.common.UserPointsDTO;
import com.marcoandbreno.completethequest.repository.UserPointsRepository;
import com.marcoandbreno.completethequest.repository.UserRepository;

@Service
public class UserPointsService  {

    private final UserPointsRepository userPointsRepository;
    private final UserRepository userRepository;

    public UserPointsService(UserPointsRepository userPointsRepository, UserRepository userRepository) {
        this.userPointsRepository = userPointsRepository;
        this.userRepository = userRepository;
    }

   public List<UserPointsDTO> getAllUserPoints() {
        return userPointsRepository.findAllUserPointsWithUsernames();
    }
}
