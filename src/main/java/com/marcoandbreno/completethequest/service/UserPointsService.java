package com.marcoandbreno.completethequest.service;

import java.util.List;

import org.springframework.stereotype.Service;

import com.marcoandbreno.completethequest.common.UserPointsDTO;
import com.marcoandbreno.completethequest.model.User;
import com.marcoandbreno.completethequest.model.UserPoints;
import com.marcoandbreno.completethequest.repository.UserPointsRepository;
import com.marcoandbreno.completethequest.repository.UserRepository;

import jakarta.transaction.Transactional;

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
